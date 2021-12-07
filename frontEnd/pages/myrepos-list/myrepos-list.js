// pages/myrepos-list/myrepos-list.js
const app =getApp();
Page({

    /**
     * 页面的初始数据
     */
    data: {
      // url_list : ['https://api.github.com/repos/sindresorhus/awesome', 'https://api.github.com/repos/public-apis/public-apis', 'https://api.github.com/repos/github/gitignore', 'https://api.github.com/repos/vinta/awesome-python', 'https://api.github.com/repos/jlevy/the-art-of-command-line'],
      url_list:"",
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
      var var_token =  wx.getStorageSync('token');
      // var var_token = "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";
      wx.request({
          url:app.globalData.server_url,
          method:'post',
          dataType:"json",
          data: {
              eventID: 422743326,
              eType: "GetInfo",
              eTime: 1459994552.51,
              edetail:{
                myrepos:null,
              },
              token: var_token
          },
          success: function(res) {
            console.log(res)
            var list = res.data.edetail["myrepos"]
            that.setData({
              url_list:list
            })
            that.data.url_list.forEach(element => {
              wx.request({
                url: app.globalData.server_url,
                method:'post',
                data: {
                  eventID: 422743326,
                  eType: "GetRepoMsg",
                  eTime: 1459994552.51,
                  edetail:{
                    full_name:element,
                    msg:null,
                  },
                  token: var_token
                },
                success:function(res){
                  //console.log(res)
                  that.data.repo.push(
                    {
                      full_name:res.data.edetail["msg"]["full_name"],
                      language:res.data.edetail["msg"]["language"],
                      star:res.data.edetail["msg"]["star"],
                    })
                  that.setData({
                      repo:that.data.repo
                  })
                }
              })
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