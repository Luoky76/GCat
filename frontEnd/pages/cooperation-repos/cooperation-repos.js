// pages/cooperation-repos/cooperation-repos.js
const app =getApp();
var Base64 = {

  // private property
  _keyStr: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

  // public method for encoding
  , encode: function (input) {
    var output = "";
    var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
    var i = 0;

    input = Base64._utf8_encode(input);

    while (i < input.length) {
      chr1 = input.charCodeAt(i++);
      chr2 = input.charCodeAt(i++);
      chr3 = input.charCodeAt(i++);

      enc1 = chr1 >> 2;
      enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
      enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
      enc4 = chr3 & 63;

      if (isNaN(chr2)) {
        enc3 = enc4 = 64;
      }
      else if (isNaN(chr3)) {
        enc4 = 64;
      }

      output = output +
        this._keyStr.charAt(enc1) + this._keyStr.charAt(enc2) +
        this._keyStr.charAt(enc3) + this._keyStr.charAt(enc4);
    } // Whend 

    return output;
  } // End Function encode 


  // public method for decoding
  , decode: function (input) {
    var output = "";
    var chr1, chr2, chr3;
    var enc1, enc2, enc3, enc4;
    var i = 0;

    input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");
    while (i < input.length) {
      enc1 = this._keyStr.indexOf(input.charAt(i++));
      enc2 = this._keyStr.indexOf(input.charAt(i++));
      enc3 = this._keyStr.indexOf(input.charAt(i++));
      enc4 = this._keyStr.indexOf(input.charAt(i++));

      chr1 = (enc1 << 2) | (enc2 >> 4);
      chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
      chr3 = ((enc3 & 3) << 6) | enc4;

      output = output + String.fromCharCode(chr1);

      if (enc3 != 64) {
        output = output + String.fromCharCode(chr2);
      }

      if (enc4 != 64) {
        output = output + String.fromCharCode(chr3);
      }

    } // Whend 

    output = Base64._utf8_decode(output);

    return output;
  } // End Function decode 


  // private method for UTF-8 encoding
  , _utf8_encode: function (string) {
    var utftext = "";
    string = string.replace(/\r\n/g, "\n");

    for (var n = 0; n < string.length; n++) {
      var c = string.charCodeAt(n);

      if (c < 128) {
        utftext += String.fromCharCode(c);
      }
      else if ((c > 127) && (c < 2048)) {
        utftext += String.fromCharCode((c >> 6) | 192);
        utftext += String.fromCharCode((c & 63) | 128);
      }
      else {
        utftext += String.fromCharCode((c >> 12) | 224);
        utftext += String.fromCharCode(((c >> 6) & 63) | 128);
        utftext += String.fromCharCode((c & 63) | 128);
      }

    } // Next n 

    return utftext;
  } // End Function _utf8_encode 

  // private method for UTF-8 decoding
  , _utf8_decode: function (utftext) {
    var string = "";
    var i = 0;
    var c, c1, c2, c3;
    c = c1 = c2 = 0;

    while (i < utftext.length) {
      c = utftext.charCodeAt(i);

      if (c < 128) {
        string += String.fromCharCode(c);
        i++;
      }
      else if ((c > 191) && (c < 224)) {
        c2 = utftext.charCodeAt(i + 1);
        string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
        i += 2;
      }
      else {
        c2 = utftext.charCodeAt(i + 1);
        c3 = utftext.charCodeAt(i + 2);
        string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
        i += 3;
      }

    } // Whend 

    return string;
  } // End Function _utf8_decode 

}
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
    // full_name:"sindresorhus/awesome",
    full_name:"",
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
    pull_request_list:[],
    collaborator_list:[],
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    var var_token =  wx.getStorageSync('token');
    // var var_token = "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";
    var value = options.full_name;
    console.log(value)
    that.setData({
      full_name:value
    })
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
      url: app.globalData.server_url,
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
        if(res.data.edetail === "yes"){
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
      url: app.globalData.server_url,
      method:'post',
      // header:{
      //   "Authorization": "token ghp_16C7e42F292c6912E7710c838347Ae178B4a"
      // },
      data: {
        eventID: 422743326,
        eType: "GetRepoMsg",
        eTime: 1459994552.51,
        edetail:{
          full_name:that.data.full_name,
          msg:null,
        },
        token: var_token
      },
      success:function(res){
        console.log(res)
        var value = res;
        that.setData({
          avatar_url:value.data.edetail["msg"]["avatar_url"],
          create_time:value.data.edetail["msg"]["create_time"],
          subscribers_count:value.data.edetail["msg"]["subscribers_count"],
          stargazers_count:value.data.edetail["msg"]["star"],
          default_branch:value.data.edetail["msg"]["default_branch"],
        })
      }
    })
    wx.request({
      url: app.globalData.server_url,
      method:'post',
      data: {
        eventID: 422743326,
        eType: "GetRepoReadme",
        eTime: 1459994552.51,
        edetail:{
          full_name:that.data.full_name,
          msg:null,
        },
        token: var_token
      },
      success:function(res){
        console.log(res)
        // console.log(atob(res.data.edetail["msg"]))
        // let value =atob(res.data.edetail["msg"]);
        let value = (Base64.decode(res.data.edetail["msg"]))
        console.log(value)
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
      url: app.globalData.server_url,
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
        console.log(res)
        var dirlist=[]
        var filelist=[]
        var result = res.data.edetail
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
    wx.request({
      url: app.globalData.server_url,
      method:'post',
      dataType:"json",
      data:{
        token: var_token,
        eventID: 422743326,
        eType: "GetRepoInfo",
        eTime: 1459994552.51,
        edetail:{
          full_name:that.data.full_name,
          pull_request_list:null,
          collaborator_list:null,
        },
      },
      success:function(res){
        var pull_request=[]
        var collaborator=[]
        pull_request = res.data.edetail["pull_request_list"]
        collaborator = res.data.edetail["collaborator_list"]
        that.setData({
          pull_request_list:pull_request,
          collaborator_list:collaborator,
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
    var var_token =  wx.getStorageSync('token');
    // var var_token = "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";
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
      url: app.globalData.server_url,
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
      url: '../dir/dir?item='+item+'&user='+that.data.user+'&reponame='+that.data.reponame+'&before='+"",
    })
  },
  tofile:function(e){
    let item = e.currentTarget.dataset.item;
    var that = this;
    console.log(item)
    console.log(that.data.user)
    console.log(that.data.reponame)
    wx.navigateTo({
      url: '../file/file?item='+item+'&user='+that.data.user+'&reponame='+that.data.reponame+'&before='+"",
    })
  }
})