import os
from pathlib import Path
import json
from typing import Any
from markupsafe import Markup


class Vite:

    @staticmethod
    def vite(entry: str):
        return Markup(f""" 
            {Vite.jsTag(entry)}\n
            {Vite.jsPreloadImports(entry)}\n
            {Vite.cssTag(entry)}
        """)

    @staticmethod
    def isDev() -> bool:
        return os.getenv("APP_ENV") != "production"

    @staticmethod
    def URL():
        host = os.getenv("VITE_HOST", 'localhost')
        port = os.getenv("VITE_PORT", 5133)
        src = os.getenv("VITE_SRC")
        if src != None :
            return f"http://{host}:{port}/{src}"
        return f"http://{host}:{port}"
        

    @staticmethod
    def getManifest() -> dict[str, Any]:
        f = open(Path(os.getcwd(), 'public/manifest.json'),'r')
        content = f.read()
        return json.loads(content)

    @staticmethod
    def importsUrls(entry: str):
        urls: list[str] = []
        manifest = Vite.getManifest()
        if 'imports' in manifest.get(entry):
            for imports in manifest.get(entry).keys():
                urls.append(manifest.get(imports)['file'])
        return urls

    @staticmethod
    def assetUrl(entry: str):
        manifest: dict[str, Any] = Vite.getManifest()
        return manifest.get(entry)['file'] if entry in manifest.keys() else ''

    @staticmethod
    def cssUrls(entry: str):
        manifest: dict[str, Any] = Vite.getManifest()
        urls: list[str] = []
        if 'css' in manifest.get(entry):
            csss: list[str] =  manifest.get(entry)['css']
            for css in csss :
                urls.append(css)
        elif "style.css" in manifest.keys() :
            css = manifest.get("style.css")["file"]
            urls.append(css)
        return urls

    @staticmethod
    def cssTag(entry: str):
        if Vite.isDev():
            return ''
        tags: str = ''
        for url in Vite.cssUrls(entry):
            tags += f"""<link rel="stylesheet" href="{url}">"""
        return tags

    @staticmethod
    def jsTag(entry: str):
        if Vite.isDev():
            url = Vite.URL()
            tag = "{}"
            return f""" 
                <script>
                    window.$RefreshReg$ = () => {tag}
                    window.$RefreshSig$ = () => (type) => type
                    window.__vite_plugin_react_preamble_installed__= true
                </script>
                
                <script type="module"  src="{url}/{entry}"></script>
            """
        url = Vite.assetUrl(entry)
        return f"""
            <script type="module" crossorigin src="{url}"></script>
        """

    @staticmethod
    def jsPreloadImports(entry: str):
        if Vite.isDev():
            return ''
        res: str = ''
        for url in Vite.importsUrls(entry):
            res += f"""<link rel="modulepreload" href="{url}">"""
        return res
