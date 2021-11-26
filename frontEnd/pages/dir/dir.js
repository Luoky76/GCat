// pages/dir/dir.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        dir_list:[],
        file_list:[],
        user:"",
        reponame:"",
        filepath:"",
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
<<<<<<< HEAD
        console.log(that.data.filepath)
        console.log(that.data.user)
        console.log(that.data.reponame)
        // var var_token =  wx.getStorageSync('token');
        var var_token = "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";
=======
>>>>>>> b8ebabae108a23f3b57e1fc893d447860447c7b9
        wx.request({
            url: 'http://127.0.0.1:5000//GcatServer',
            method:'post',
            dataType:"json",
            data:{
              token: var_token,
              eventID: 422743326,
              eType: "GetFile",
              eTime: 1459994552.51,
<<<<<<< HEAD
              edetail:{
                username:that.data.user,
                reponame:that.data.reponame,
                filepath:that.data.filepath,
                type:"dir"
=======
              eDetail:{
                username:that.data.user,
                reponame:that.data.reponame,
                filepath:that.data.filepath
>>>>>>> b8ebabae108a23f3b57e1fc893d447860447c7b9
              },
            },
            success:function(res){
              var dirlist=[]
              var filelist=[]
              var result = res.data.eDetail
              for (var key in result)
              {
                if(result[key] === "file")
                {
<<<<<<< HEAD
                  filelist.push(key);
=======
                  filelist.pus(key);
>>>>>>> b8ebabae108a23f3b57e1fc893d447860447c7b9
                }
                else if(result[key] === "dir")
                {
                  dirlist.push(key);
                }
              }
              that.setData({
                file_list:filelist,
                dir_list:dirlist,
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

<<<<<<< HEAD
    },
    todir:function(e){
      let item = e.currentTarget.dataset.item;
      var that = this;
      wx.navigateTo({
        url: '../dir/dir?item='+item+'&user='+that.data.user+'&reponame'+that.data.reponame,
      })
    },
    tofile:function(e){
      let item = e.currentTarget.dataset.item;
      wx.navigateTo({
        url: '../file/file?item='+item+'&user='+that.data.user+'&reponame'+that.data.reponame,
      })
=======
>>>>>>> b8ebabae108a23f3b57e1fc893d447860447c7b9
    }
})