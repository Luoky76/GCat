Page({
<<<<<<< HEAD

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
=======
 
  data: {
  show:false,//控制下拉列表的显示隐藏，false隐藏、true显示
  List1:['user1','user2','user3','user4'],//下拉列表的数据
  List2:['public','private'],
  index:0,//选择的下拉列表下标
  nub:0
  },
  // 点击下拉显示框
  selectTap(){
  this.setData({
   show: !this.data.show
  });
  },
  // 点击下拉列表
  optionTap(e){
  let Index=e.currentTarget.dataset.index;//获取点击的下拉列表的下标
  this.setData({
   index:Index,
   show:!this.data.show
  });
  },

  onLoad: function (options) {
   
  },
  
  bindPickerChange: function (e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      nub: e.detail.value
    })
  },
  bindButtonTap:function(){
    this.setData({
      focus:true
    })
  },
  bindKeyInput:function(e){
    this.setData({
      inputValue:e.detail.value
    })
  },
  bindHideKeyboard:function(e){
    if(e.detail.value === "close"){
      //收起键盘
      wx.hideKeyboard();
    }
  }
 })
>>>>>>> b8ebabae108a23f3b57e1fc893d447860447c7b9
