// pages/file/file.js
var app = getApp()
Page({

    /**
     * 页面的初始数据
     */
    data: {
        user:"",
        reponame:"",
        filepath:"",
        code:"",
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        var that = this;
        var v1 = options.item;
        var v2 = options.user;
        var v3 = options.reponame;
        that.setData({
            filepath:v1,
            user:v2,
            reponame:v3,
        })
        var var_token =  wx.getStorageSync('token');
        // var var_token = "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";
        wx.request({
            url: 'http://127.0.0.1:5000//GcatServer',
            method:'post',
            dataType:"json",
            data:{
              token: var_token,
              eventID: 422743326,
              eType: "GetFile",
              eTime: 1459994552.51,
              edetail:{
                username:that.data.user,
                reponame:that.data.reponame,
                filepath:that.data.filepath,
                type:"file"
              },
            },
            success:function(res){
              let rescode="";
              rescode = app.towxml.toJson(res.data.edetail, 'bytes');
              that.setData({
                code:rescode,
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

    }
})