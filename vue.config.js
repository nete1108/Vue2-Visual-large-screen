const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer:{
    proxy:{
      '/api1':{
        target:'http://localhost:5000',
        changeOrigin:true,
        pathRewrite:{'^/api1':''}
      },
      '/api2':{
        target:'http://localhost:8080',
        changeOrigin:true,
        pathRewrite:{'^/api2':''}
      }
    }
  }
})

