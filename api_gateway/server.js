const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();
const PORT = 3000;

// Define your proxy routes
app.use('/api', createProxyMiddleware({
    target: 'http://backend:8000',  // Change target to your backend URL
    changeOrigin: true,
    pathRewrite: {
        '^/api': '',  // Remove /api from the forwarded URL
    },
}));

// Start the server
app.listen(PORT, () => {
    console.log(`API Gateway running on port ${PORT}`);
});
