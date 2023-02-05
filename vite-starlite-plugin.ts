import fs from "fs";
import { join, resolve } from "path";
import { PluginOption, ResolvedConfig } from "vite";
import FullReload from "vite-plugin-full-reload";

export default function ViteStarlitePlugin(config?: {
  base?: string;
  root?: string;
  public?: string;
  entry?: string;
  output?: string;
  port?: number;
  host?: string; 
  apiServer?: string;
  isHttps?: boolean;
}): PluginOption {
  const pluginConfig = {
    base: config?.base ?? "static",
    root: config?.root ?? "ressources/assets/js",
    public: config?.public ?? "public",
    entry: config?.entry ?? "index.tsx",
    output: config?.output ?? `${config?.base ?? "static"}/js/bundle`,
    port: config?.port ?? 5133,
    host: config?.host ?? "localhost",
    apiServer: config?.apiServer ?? "http://localhost:8000",
    isHttps: config?.isHttps ?? false, 
  };
  let resolvedConfig: ResolvedConfig;
  return {
    name: "vite-starlite-plugin",
    config(config) {
      return {
        ...config,
        base: `./${config?.base ?? ''}`,
        root: pluginConfig.root,
        publicDir: pluginConfig.public,
        define: {
          "process.env.NODE_ENV": null,
        },
        server: {
          origin: "__starlite_vite_placeholder__",
          port: pluginConfig.port,
          host: pluginConfig.host,
          strictPort: true,
          middlewareMode: false,
          // open: join(__dirname, 'dev-server-index.html'),
          open: false,
          proxy: {
            "/api": {
              target: pluginConfig.apiServer,
              changeOrigin: true,
              //   rewrite: (path) => path.replace(/^\/api/, ""),
            },
          },
        },
        optimizeDeps: {
          entries: [resolve(pluginConfig.root, pluginConfig.entry)],
        },
        build: {
          assetsDir: pluginConfig.output,
          manifest: true,
          emptyOutDir: false,
          outDir: resolve(pluginConfig.public),
          rollupOptions: {
            external: ["React", "Vue"],
            input: resolve(pluginConfig.root, pluginConfig.entry),
            cache: false,
            output: {
              format: "cjs",
              // manualChunks:  () => 'app.js',
              assetFileNames: (assetInfo) => {
                if (assetInfo.name === "style.css") {
                  return `${pluginConfig.output}/app.css`;
                }
                return `${pluginConfig.output}/${assetInfo.name}` ?? "app.js";
              },
            },
          },
        },
        plugins: [FullReload([join(process.cwd(), "vite.config.ts")])],
      };
    },
    configResolved(config) {
      resolvedConfig = config;
    },
    transform(code) {
      if (resolvedConfig.command === "serve") {
        return code.replace(
          /__starlite_vite_placeholder__/g,
          `${pluginConfig.isHttps ? "https" : "http"}://${pluginConfig.host}:${
            pluginConfig.port
          }`
        );
      }
    },
    configureServer(server) {
      server.httpServer?.once("listening", () => {
        const address = server.httpServer?.address();
        console.log("Address : ", address);
      });
      const envDir = resolvedConfig.envDir || process.cwd();
      return () =>
        server.middlewares.use((req, res, next) => {
          if (req.url === "/index.html") {
            res.statusCode = 200;
            const content = fs.readFileSync(
              join(__dirname, "dev-server-index.html")
            );
            res.end(content);
          }
          next();
        });
    },
  };
}
