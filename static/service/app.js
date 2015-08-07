/**
 * Created by babbarshaer on 2015-08-07.
 */
(function(){

    var app = angular.module('shortener',[]);

    app.config(['$logProvider', function($logProvider){
        $logProvider.debugEnabled(true);
    }])

}());