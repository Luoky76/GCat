// pages/repos/repos.js
var app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    /** 
     * 页面配置 
     */
    winWidth: 0,
    winHeight: 0,
    currentTab: 0,
    full_name:"sindresorhus/awesome",
    // full_name:"",
    avatar_url:"",
    user:"",
    reponame:"",
    create_time:"",
    subscribers_count:"",
    stargazers_count:"",
    readme:"",
    default_branch:"",
    download_url:"",
    starsrc:"",
    hasstar:"",
    file_list:[],
    dir_list:[],
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    // var map = {'.editorconfig': 'file', '.gitattributes': 'file', '.github': 'dir', 'awesome.md': 'file', 'code-of-conduct.md': 'file', 'contributing.md': 'file', 'create-list.md': 'file', 'license': 'file', 'media': 'dir', 'pull_request_template.md': 'file', 'readme.md': 'file'};
    // var dirlist=[]
    // var filelist=[]
    // for (var key in map)
    // {
    //   if(map[key] === "file")
    //   {
    //     filelist.push(key);
    //   }
    //   else if(map[key] === "dir")
    //   {
    //     dirlist.push(key);
    //   }
    // }
    // console.log(dirlist)
    // console.log(filelist)
    // this.setData({
    //   file_list:filelist,
    //   dir_list:dirlist,
    // })
    var that = this;
    // var var_token =  wx.getStorageSync('token');
    var var_token = "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";
    // var value = options.full_name;
    // console.log(value)
    // that.setData({
    //   full_name:value
    // })
    var strs= new Array();
    strs=this.data.full_name.split("/"); 
    that.setData({
      user:strs[0],
      reponame:strs[1]
    })
    /** 
     * 获取系统信息 
     */
    wx.getSystemInfo({
      success: function (res) {
        that.setData({
          winWidth: res.windowWidth,
          winHeight: res.windowHeight
        });
      }
    });
    wx.request({
      url: 'http://127.0.0.1:5000//GcatServer',
      method:'post',
      dataType:"json",
      data: {
        token: var_token,
        eventID: 422743326,
        eType: "CheckStar",
        eTime: 1459994552.51,
        edetail:{
          full_name:that.data.full_name
        },
      },
      success:function(res){
        if(res === "yes"){
          that.setData({
            starsrc:"/pages/images/star0.png",
            hasstar:"yes"
          })
        }
        else{
          that.setData({
            starsrc:"/pages/images/star.png"
          })
        }
      }
    })
    wx.request({
      url: 'https://api.github.com/repos/'+that.data.full_name,
      method:'get',
      // header:{
      //   "Authorization": "token ghp_16C7e42F292c6912E7710c838347Ae178B4a"
      // },
      data: {
        token: var_token
      },
      success:function(res){
        console.log(res)
        var value = res;
        that.setData({
          avatar_url:value.data.owner.avatar_url,
          create_time:value.data.created_at,
          subscribers_count:value.data.subscribers_count,
          stargazers_count:value.data.stargazers_count,
          default_branch:value.data.default_branch,
        })
      }
    })
    wx.request({
      url: "https://api.github.com/repos/"+that.data.full_name+"/readme",
      method:'get',
      data: {
        token: var_token
      },
      success:function(res){
        console.log(res)
        console.log(atob(res.data.content))
        let value =atob(res.data.content);
        let data = app.towxml.toJson(
          value,               // `markdown`或`html`文本内容
          'markdown',             // `markdown`或`html`
          that                     // 当前页面的`this`（2.1.0或以上的版本该参数不可省略）
        );
        that.setData({
          readme:data
        })
      }
    })
    wx.request({
      url: 'http://127.0.0.1:5000//GcatServer',
      method:'post',
      dataType:"json",
      data:{
        token: var_token,
        eventID: 422743326,
        eType: "GetFileList",
        eTime: 1459994552.51,
        edetail:{
          username:strs[0],
          reponame:strs[1]
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
            filelist.push(key);
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

  },
  /** 
   * 滑动切换tab 
   */
  bindChange: function (e) {
    var that = this;
    that.setData({
      currentTab: e.detail.current
    });
  },
  /** 
   * 点击tab切换 
   */
  swichNav: function (e) {
    var that = this;
    if (this.data.currentTab === e.target.dataset.current) {
      return false;
    } else {
      that.setData({
        currentTab: e.target.dataset.current
      })
    }
  },
  starred:function(){
    var that = this;
    // var var_token =  wx.getStorageSync('token');
    var var_token = "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";
    var type;
    if(this.data.hasstar === "yes")
    {
      that.setData({
        hasstar:"no"
      })
      type = "DeclineStar"
    }
    else
    {
      that.setData({
        hasstar:"yes"
      })
      type = "Star"
    }
    wx.request({
      url: 'http://127.0.0.1:5000//GcatServer',
      method:'post',
      dataType:"json",
      data: {
        token: var_token,
        eventID: 422743326,
        eType: type,
        eTime: 1459994552.51,
        edetail:{
          full_name:that.data.full_name
        },
      },
      success:function(res){
        if(type === "Star"){
          that.setData({
            starsrc:"/pages/images/star0.png"
          })
        }
        else{
          that.setData({
            starsrc:"/pages/images/star.png"
          })
        }
      }
    })
  },
  todir:function(e){
    let item = e.currentTarget.dataset.item;
    var that = this;
    console.log(item)
    console.log(that.data.user)
    console.log(that.data.reponame)
    wx.navigateTo({
      url: '../dir/dir?item='+item+'&user='+that.data.user+'&reponame='+that.data.reponame,
    })
  },
  tofile:function(e){
    let item = e.currentTarget.dataset.item;
    console.log(item)
    console.log(that.data.user)
    console.log(that.data.reponame)
    wx.navigateTo({
      url: '../file/file?item='+item+'&user='+that.data.user+'&reponame='+that.data.reponame,
    })
  }
})