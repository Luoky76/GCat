// pages/personal/personal.js
const app =getApp();
Page({

    /**
     * 页面的初始数据
     */
    data: {
        avatar_url :"",
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        var that = this;
        var var_token =  wx.getStorageSync('token');
        wx.request({
            url: app.globalData.server_url,
            method:'post',
            dataType:"json",
            data: {
              token: var_token,
              eventID: 422743326,
              eType: "GetUserAvatar",
              eTime: 1459994552.51,
              edetail:{},
            },
            success:function(res){
              that.setData({
                avatar_url:res.data.edetail
              })
              wx.setStorageSync('avatar_url', that.data.avatar_url)
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

})