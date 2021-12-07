// pages/message/message.js
const app =getApp();
Page({

    /**
     * 页面的初始数据
     */
    data: { 
        dropdownData:["事件","类型","时间"],
        selectData: ['事件1', '事件2', '事件3'], 
        sort_hidden: true,
        zhezhao:true,
        dropup_pic_index: true,
        event_list:[],
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
        // var var_token = "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"
        var that = this
        wx.request({
            url: app.globalData.server_url,
            method:'post',
            dataType:"json",
            data: {
                eventID: 422743326,
                eType: "GetInfo",
                eTime: 1459994552.51,
                edetail:{
                  newEvents:null,
                },
                token: var_token
            },
            success: function(res) {
              console.log(res)
              var list = res.data.edetail["newEvents"]["eventList"]
              that.setData({
                event_list:list
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