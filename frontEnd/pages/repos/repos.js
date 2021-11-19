// pages/repos/repos.js
var app = getApp()
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
    currentTab: 0,
    // full_name:"sindresorhus/awesome",
    full_name:"",
    avatar_url:"",
    user:"",
    create_time:"",
    watchers:"",
    stargazers_count:"",
    readme:"",
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    var var_token =  wx.getStorageSync('token');
    // var var_token = "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";
    var value = options.full_name;
    that.setData({
      full_name:value
    })
    var strs= new Array();
    strs=this.data.full_name.split("/"); 
    that.setData({
      user:strs[0]
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
      url: 'https://api.github.com/repos/'+that.data.full_name,
      method:'get',
      // header:{
      //   "Authorization": "token ghp_16C7e42F292c6912E7710c838347Ae178B4a"
      // },
      success:function(res){
        console.log(res)
        var value = res;
        that.setData({
          avatar_url:value.data.owner.avatar_url,
          create_time:value.data.created_at,
          watchers:value.data.watchers,
          stargazers_count:value.data.stargazers_count,
        })
      }
    })
    wx.request({
      url: 'https://raw.githubusercontent.com/'+that.data.full_name+"/master/README.md",
      method:'get',
      success:function(res){
        console.log(res)
        let value = res;
        that.setData({
          readme:value.data
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