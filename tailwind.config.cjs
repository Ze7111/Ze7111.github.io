/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme')
module.exports = {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	theme: {
		screens: {
			'xs': '424px',
			...defaultTheme.screens,
		  },
		extend: {
			colors: {
				background: ['#4444'],
				primary: ['#5558DA'],
				secondary: ['#18181B'],
				accent: ['#5FD1F9'],
			},
			fontFamily: {
				sans: [("Inter", "sans-serif"), ("Helvetica", "sans-serif")],
			  },
			}
		},
	plugins: [ require('autoprefixer'), require('cssnano'), require('@tailwindcss/typography')],
}
