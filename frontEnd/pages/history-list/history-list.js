// pages/history-list/history-list.js
const app =getApp();
Page({

    /**
     * 页面的初始数据
     */
    data: { 
        dropdownData:["语言","时间"],
        selectData: ['事件1', '事件2', '事件3'], 
        sort_hidden: true,
        zhezhao:true,
        dropup_pic_index: true,
        repo:[],
        }, 

        
        dropdownTap(e){ 
        let _this=this; 
        _this.setData({ 
        id: e.currentTarget.dataset.index,
        sort_hidden:false,
        zhezhao: false, 
        upordown: "up", 
        }) 
        },
        
        optionTap(e) { 
        let _that=this; 
        _that.setData({ 
        key: e.currentTarget.dataset.index, 
        zhezhao: true, 
        sort_hidden: true,
        upordown: "down", 
        })
        },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        var var_token =  wx.getStorageSync('token')
        var _this = this;
        var that = this;    
        wx.request({
            url: app.globalData.server_url,
            method:'post',
            dataType:"json",
            data: {
                eventID: 422743326,
                eType: "GetHistory",
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
                  console.log(element)
                  console.log(element[0].trim())
                  wx.request({
                    url: app.globalData.server_url,
                    method:'post',
                    data: {
                      eventID: 422743326,
                      eType: "GetRepoMsg",
                      eTime: 1459994552.51,
                      edetail:{
                        full_name:element[0].trim(),
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
      }
})