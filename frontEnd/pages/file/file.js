// pages/file/file.js
<<<<<<< HEAD
var app = getApp()
=======
>>>>>>> b8ebabae108a23f3b57e1fc893d447860447c7b9
Page({

    /**
     * 页面的初始数据
     */
    data: {
<<<<<<< HEAD
        user:"",
        reponame:"",
        filepath:"",
        code:"",
=======

>>>>>>> b8ebabae108a23f3b57e1fc893d447860447c7b9
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
<<<<<<< HEAD
        // var that = this;
        // var v1 = options.item;
        // var v2 = options.user;
        // var v3 = options.reponame;
        // that.setData({
        //     filepath:v1,
        //     user:v2,
        //     reponame:v3,
        // })
        // // var var_token =  wx.getStorageSync('token');
        // var var_token = "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";
        // wx.request({
        //     url: 'http://127.0.0.1:5000//GcatServer',
        //     method:'post',
        //     dataType:"json",
        //     data:{
        //       token: var_token,
        //       eventID: 422743326,
        //       eType: "GetFile",
        //       eTime: 1459994552.51,
        //       edetail:{
        //         username:that.data.user,
        //         reponame:that.data.reponame,
        //         filepath:that.data.filepath,
        //         type:"file"
        //       },
        //     },
        //     success:function(res){
        //       let rescode="";
        //       rescode = app.towxml.toJson(res.data.eDetail, 'bytes');
        //       that.setData({
        //         code:rescode,
        //       })
        //     }
        //   })
        var test = "from flask import Flask, request, jsonify\nfrom gevent import GEvent\nfrom handlers import EventDistributer\n\napp = Flask(__name__)\n\n\n@app.route('/GcatServer', methods=['POST', 'GET'])\ndef main():\n    gEvent = GEvent(dict(request.get_json()))  # \xe6\x8f\x90\xe5\x8f\x96\xe6\x8a\xa5\xe6\x96\x87GEvent\xe4\xbf\xa1\xe6\x81\xaf\n    gEvent = EventDistributer(gEvent)  # \xe5\x88\x86\xe5\x8f\x91\xe8\x8e\xb7\xe5\x8f\x96\xe9\x9c\x80\xe6\xb1\x82\xe5\x86\x85\xe5\xae\xb9\n    return jsonify(gEvent.toJson())  # \xe8\xbf\x94\xe5\x9b\x9ejson\xe6\x8a\xa5\xe6\x96\x87\n\n\nif __name__ == '__main__':\n    # \xe5\xa4\x9a\xe7\xba\xbf\xe7\xa8\x8b\xe5\x90\xaf\xe5\x8a\xa8\xe5\x90\x8e\xe7\xab\xaf\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\n    app.run(debug=True, threaded=True)\n"
        let data = app.towxml.toJson(test,'markdown');
        console.log(data);
        this.setData({
            code:data,
        })
=======

>>>>>>> b8ebabae108a23f3b57e1fc893d447860447c7b9
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