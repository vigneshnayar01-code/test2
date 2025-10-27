# V04 UI Change - Website

This repository contains static HTML/CSS files and a small Express server to host them. It's configured for deployment on Vercel using a Node server.

Quick setup (PowerShell):

1. Install dependencies

```powershell
cd "e:\Vijay\Project\Vignesh\v04-UI change\website"
npm install
```

2. Run locally

```powershell
npm start
# or for auto-restart during development
npm run dev
```

Visit http://localhost:3000

3. Deploy to Vercel

- Install Vercel CLI (optional): `npm i -g vercel`
- From the project folder run: `vercel` and follow prompts, or connect this repo in the Vercel dashboard.

Notes
- The Express server serves static files from the project root. Vercel will run `server.js` as a Node function via the configuration in `vercel.json`.
