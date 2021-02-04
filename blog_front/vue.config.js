module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://www.oslozone.cn/api',
        changeOrigin: true,
        ws: true,
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  },
  runtimeCompiler: true,
  productionSourceMap: false,
  publicPath: './',
  outputDir: '../dist',
  lintOnSave: false,
  configureWebpack: {
    performance: {
      hints: 'warning',
      maxEntrypointSize: 50000000,
      maxAssetSize: 30000000,
      assetFilter: function (assetFilename) {
        return assetFilename.endsWith('.js')
      }
    }
  }
}
