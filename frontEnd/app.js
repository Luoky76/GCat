// app.js
const Towxml = require('/towxml/main'); 
App({
  onLaunch() {
    // 展示本地存储能力
    const logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)

    // 登录
    wx.login({
      success: res => {
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
      }
    })
  },
  globalData: {
    userInfo: null,
    server_url : 'https://www.rat403.cn//GcatServer',
    // server_url : 'http://127.0.0.1:5000//GcatServer',
  },
  towxml:new Towxml()   
})
