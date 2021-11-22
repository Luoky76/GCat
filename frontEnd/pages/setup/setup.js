Page({
 
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
