/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./ressources/views/app.html.jinja",
    "./dev-server-index.html",
    "./ressources/assets/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
