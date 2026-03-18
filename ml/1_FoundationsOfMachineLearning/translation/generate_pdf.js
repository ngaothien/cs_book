const fs = require('fs');
const marked = require('marked');
const puppeteer = require('puppeteer');

(async () => {
    try {
        const md = fs.readFileSync('18_translation.md', 'utf-8');
        const htmlContent = marked.parse(md);
        
        const fullHtml = `
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; padding: 40px; }
                h1, h2, h3 { color: #333; }
                p { line-height: 1.6; }
            </style>
        </head>
        <body>
            ${htmlContent}
        </body>
        </html>
        `;
        
        fs.writeFileSync('temp.html', fullHtml);
        
        const browser = await puppeteer.launch({ headless: 'new' });
        const page = await browser.newPage();
        await page.goto('file://' + process.cwd() + '/temp.html', { waitUntil: 'networkidle0' });
        await page.pdf({ path: '18_translation.pdf', format: 'A4', printBackground: true, margin: { top: '20px', bottom: '20px', left: '20px', right: '20px' } });
        
        await browser.close();
        fs.unlinkSync('temp.html');
        console.log("PDF generated successfully: 18_translation.pdf");
    } catch (e) {
        console.error("Error:", e);
    }
})();
