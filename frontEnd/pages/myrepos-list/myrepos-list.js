// pages/myrepos-list/myrepos-list.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
      url_list : ['https://api.github.com/repos/sindresorhus/awesome', 'https://api.github.com/repos/public-apis/public-apis', 'https://api.github.com/repos/github/gitignore', 'https://api.github.com/repos/vinta/awesome-python', 'https://api.github.com/repos/jlevy/the-art-of-command-line'],
      // list:"",
    },
    myrepos:function(){
        wx.navigateTo({
           url:'/pages/my-repos/my-repos',
        })
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

    }
})