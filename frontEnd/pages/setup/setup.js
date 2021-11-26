Page({

  /**
   * 页面的初始数据
   */
  data: {
    chosen: '',
    path_dict : {},
  },

  formSubmit(e) {
    console.log('form发生了submit事件，携带数据为：', e.detail.value)
    // console.log(e.detail)
    var data = e.detail.value["input"]
    var name = e.detail.value["repo"]
    var strs=data.split(";");
    var path = {};
    for (let i = 0; i < strs.length; i++) 
    {
      // console.log(strs[i])
      var eachstr = strs[i].split(":");
      // console.log(eachstr[0]);
      var eachpath = eachstr[1].split(",");
      path[eachstr[0]]=[];
      for(let j = 0; j < eachpath.length; j++)
      {
        path[eachstr[0]].push(eachpath[j]);
      }
      console.log(path[eachstr[0]])
    }
    this.setData({
      path_dict:path
    })
    var that = this;
    // var var_token =  wx.getStorageSync('token');
    var var_token = "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";
    wx.request({
      url: 'http://127.0.0.1:5000//GcatServer',
      method:'post',
      dataType:"json",
      data:{
        token: var_token,
        eventID: 422743326,
        eType: "CreateRepo",
        eTime: 1459994552.51,
        edetail:{
          reponame:name,
          file_dict:path,
        },
      },
      success:function(res){
        wx.navigateBack();
      }
    })
  },

  formReset(e) {
    console.log('form发生了reset事件，携带数据为：', e.detail.value)
    this.setData({
      chosen: ''
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

  },
})
