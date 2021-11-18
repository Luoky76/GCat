Page({

  data: {
  show:false,//控制下拉列表的显示隐藏，false隐藏、true显示
  List0:['user1', 'user2', 'user3', 'user4'],
  List1:['Public', 'Private'],
  index1: 0,
  index2: 0,
  },
  // 点击下拉显示框
  selectTap(){
  this.setData({
   show: !this.data.show
  });
  },
  // 点击下拉列表
  optionTap(e){
  let Index1=e.currentTarget.dataset.index1;//获取点击的下拉列表的下标
  let Index2=e.currentTarget.dataset.index2;//获取点击的下拉列表的下标
  this.setData({
   index1:Index1,
   index2:Index2,
   show:!this.data.show
  });
  },
  bindPickerChange: function (e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      index: e.detail.value
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