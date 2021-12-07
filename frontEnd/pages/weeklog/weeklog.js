// pages/weeklog/weeklog.js
const app =getApp();
Page({

    /**
     * 页面的初始数据
     */
    data: {
        /** 
     * 页面配置 
     */
    winWidth: 0,
    winHeight: 0,
    // tab切换  
    currentTab: 0,
    count1:null,
    count2:null,
    count3:null,
    avatar_url:""
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        var that = this;
        var var_token =  wx.getStorageSync('token')
        var avatar_url =  wx.getStorageSync('avatar_url')
        that.setData({
          avatar_url:avatar_url
        })
    /** 
     * 获取系统信息 
     */
    wx.getSystemInfo({
      success: function (res) {
        that.setData({
          winWidth: res.windowWidth,
          winHeight: res.windowHeight
        });
      }
    });
    wx.request({
      url: app.globalData.server_url,
      method:'post',
      dataType:"json",
      data: {
          eventID: 422743326,
          eType: "GetInfo",
          eTime: 1459994552.51,
          edetail:{
            newEvents:null,
            type:"push"
          },
          token: var_token
      },
      success: function(res) {
        console.log(res)
        var list = res.data.edetail["newEvents"]
        that.setData({
          count1:list["count"]
        })
      }
    })
    wx.request({
      url: app.globalData.server_url,
      method:'post',
      dataType:"json",
      data: {
          eventID: 422743326,
          eType: "GetInfo",
          eTime: 1459994552.51,
          edetail:{
            newEvents:null,
            type:"merge"
          },
          token: var_token
      },
      success: function(res) {
        console.log(res)
        var list = res.data.edetail["newEvents"]
        that.setData({
          count2:list["count"]
        })
      }
    })
    wx.request({
      url: app.globalData.server_url,
      method:'post',
      dataType:"json",
      data: {
          eventID: 422743326,
          eType: "GetInfo",
          eTime: 1459994552.51,
          edetail:{
            newRepos:null,
          },
          token: var_token
      },
      success: function(res) {
        console.log(res)
        var list = res.data.edetail["newRepos"]
        that.setData({
          count3:list["count"]
        })
      }
    })
    },

    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady: function () {

    },

    /**
     * 生命周期函数--监听页面显示
     */
    onShow: function () {

    },

    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide: function () {

    },

    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload: function () {

    },

    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh: function () {

    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom: function () {

    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage: function () {

    },
    /** 
   * 滑动切换tab 
   */
  bindChange: function (e) {
    var that = this;
    that.setData({
      currentTab: e.detail.current
    });
  },
  /** 
   * 点击tab切换 
   */
  swichNav: function (e) {
    var that = this;
    if (this.data.currentTab === e.target.dataset.current) {
      return false;
    } else {
      that.setData({
        currentTab: e.target.dataset.current
      })
    }
  }
})