// pages/login/login.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
      inputValue :""
    },
    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {

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
    
    login:function(e){
      console.log(e);
      this.setData({
        inputValue: e.detail.value
      })
    },

    log:function(){
      console.log(this.data.inputValue) 
      wx.setStorage({
        key:"token",
        data:this.data.inputValue,
        success: function() {
          console.log('写入value1成功')
          wx.switchTab({
            url:'/pages/recommend/recommend',
         })
        },
        fail: function() {
          console.log('写入value1发生错误')
        }
      })
    }
})