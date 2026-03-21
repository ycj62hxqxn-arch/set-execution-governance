// Batch HTML to PDF export using Puppeteer (Node.js)
// Usage: node html-to-pdf-batch.js [optional: directory or file list]

const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer');

async function htmlToPdf(inputPath, outputPath) {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto('file://' + inputPath, { waitUntil: 'networkidle0' });
  await page.pdf({
    path: outputPath,
    format: 'A4',
    printBackground: true,
    margin: { top: '20mm', bottom: '20mm', left: '15mm', right: '15mm' }
  });
  await browser.close();
}

async function batchExport(dir) {
  const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));
  for (const file of files) {
    const inputPath = path.resolve(dir, file);
    const outputPath = inputPath.replace(/\.html$/, '_PUPPETEER.pdf');
    console.log(`Exporting ${file} → ${path.basename(outputPath)}`);
    await htmlToPdf(inputPath, outputPath);
  }
}

// Entry point
(async () => {
  const args = process.argv.slice(2);
  let targets = args.length ? args : [process.cwd()];
  for (const target of targets) {
    const stat = fs.statSync(target);
    if (stat.isDirectory()) {
      await batchExport(target);
    } else if (stat.isFile() && target.endsWith('.html')) {
      const inputPath = path.resolve(target);
      const outputPath = inputPath.replace(/\.html$/, '_PUPPETEER.pdf');
      await htmlToPdf(inputPath, outputPath);
      console.log(`Exported ${path.basename(inputPath)} → ${path.basename(outputPath)}`);
    }
  }
})();

// Requirements:
// 1. Install Node.js (https://nodejs.org/)
// 2. Install Puppeteer: npm install puppeteer
// 3. Run: node html-to-pdf-batch.js [directory or file list]
//    (If no argument, runs in current directory)
// 4. Output PDFs will be named *_PUPPETEER.pdf
