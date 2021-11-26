// pages/myrepos-list/myrepos-list.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
      url_list : ['https://api.github.com/repos/sindresorhus/awesome', 'https://api.github.com/repos/public-apis/public-apis', 'https://api.github.com/repos/github/gitignore', 'https://api.github.com/repos/vinta/awesome-python', 'https://api.github.com/repos/jlevy/the-art-of-command-line'],
      // url_list:"",
      repo:[],
    },
    torepo:function(e){
      //console.log(e)
      let full_name = e.currentTarget.dataset.full_name;
      wx.navigateTo({
        url: '../cooperation-repos/cooperation-repos?full_name='+full_name,
      })
    },
    /**
     * 生命周期函数--监听页面加载
     */
   
    onLoad: function (options) {
      var that = this;
      // var var_token =  wx.getStorageSync('token');
      var var_token = "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";
      that.data.url_list.forEach(element => {
        wx.request({
          url: element,
          method:'get',
          data: {
            token: var_token
          },
          success:function(res){
            console.log(res)
            that.data.repo.push(
              {
                full_name:res.data.full_name,
                language:res.data.language,
                star:res.data.stargazers_count,
                url:res.data.repos_url
              })
            that.setData({
                repo:that.data.repo
            })
          }
        })
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