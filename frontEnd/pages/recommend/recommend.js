// pages/recommend/recommend.js
const app =getApp();
Page({
    
    /**
     * 页面的初始数据
     */
    data: {
        url_list:[],
        // list : ['https://api.github.com/repos/sindresorhus/awesome', 'https://api.github.com/repos/public-apis/public-apis', 'https://api.github.com/repos/github/gitignore', 'https://api.github.com/repos/vinta/awesome-python', 'https://api.github.com/repos/jlevy/the-art-of-command-line', 'https://api.github.com/repos/30-seconds/30-seconds-of-code', 'https://api.github.com/repos/microsoft/TypeScript', 'https://api.github.com/repos/animate-css/animate.css', 'https://api.github.com/repos/avelino/awesome-go', 'https://api.github.com/repos/jwasham/coding-interview-university', 'https://api.github.com/repos/kamranahmedse/developer-roadmap', 'https://api.github.com/repos/trekhleb/javascript-algorithms', 'https://api.github.com/repos/TheAlgorithms/Python', 'https://api.github.com/repos/ossu/computer-science', 'https://api.github.com/repos/jlevy/the-art-of-command-line', 'https://api.github.com/repos/microsoft/terminal', 'https://api.github.com/repos/iluwatar/java-design-patterns', 'https://api.github.com/repos/MisterBooo/LeetCodeAnimation', 'https://api.github.com/repos/axios/axios', 'https://api.github.com/repos/PanJiaChen/vue-element-admin', 'https://api.github.com/repos/netdata/netdata', 'https://api.github.com/repos/gin-gonic/gin', 'https://api.github.com/repos/httpie/httpie', 'https://api.github.com/repos/ansible/ansible', 'https://api.github.com/repos/psf/requests', 'https://api.github.com/repos/square/okhttp', 'https://api.github.com/repos/yarnpkg/yarn', 'https://api.github.com/repos/TranslucentTB/TranslucentTB', 'https://api.github.com/repos/42wim/matterbridge', 'https://api.github.com/repos/nslog11/Gitter', 'https://api.github.com/repos/AnySoftKeyboard/AnySoftKeyboard', 'https://api.github.com/repos/sozu-proxy/sozu', 'https://api.github.com/repos/fossasia/susi_gitterbot', 'https://api.github.com/repos/digicorp/propeller', 'https://api.github.com/repos/Makuna/NeoPixelBus', 'https://api.github.com/repos/sierra-library/sierra'],
        repo:[],
        inputValue:"",
    },
    bindKeyInput: function (e) {
      this.setData({
        inputValue: e.detail.value
      })
      console.log(e.detail.value)
    },
    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
      var var_token =  wx.getStorageSync('token')
      var _this = this;
      wx.request({
          url: app.globalData.server_url,
          method:'post',
          dataType:"json",
          data: {
              eventID: 422743326,
              eType: "Recommend",
              eTime: 1459994552.51,
              edetail:{},
              token: var_token
          },
          success: function(res) {
            _this.setData({
              url_list : res.data.edetail
            });
            console.log(_this.data.url_list);
            var that = _this;
            _this.data.url_list.forEach(element => {
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
    onReady: function () {},

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

    torepo:function(e){
      //console.log(e)
      var var_token =  wx.getStorageSync('token')
      var that = this;
      let full_name = e.currentTarget.dataset.full_name;
      wx.request({
        url: app.globalData.server_url,
        method:'post',
        data: {
          eventID: 422743326,
          eType: "SetHistory",
          eTime: 1459994552.51,
          edetail:{
            full_name:full_name,
          },
          token: var_token
        },
        success:function(res){
          console.log(res)
        }
      })
      wx.navigateTo({
        url: '../repos/repos?full_name='+full_name,
      })
    },
    search:function(){
      var var_token =  wx.getStorageSync('token')
      var that = this;
      var _this = this;
      if(that.data.inputValue)
      {
      wx.request({
        url: app.globalData.server_url,
        method:'post',
        data: {
          eventID: 422743326,
          eType: "SearchRepo",
          eTime: 1459994552.51,
          edetail:{
            name:that.data.inputValue
          },
          token: var_token
        },
        success:function(res){
          console.log(res)
          _this.setData({
            url_list : res.data.edetail
          });
          console.log(_this.data.url_list);
          var that = _this;
          _this.data.url_list.forEach(element => {
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
                  that.setData({
                    repo:[]
                })
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
    }
    else{
      that.onLoad()
    }
    }
})