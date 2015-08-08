/**
 * Created by babbar on 2015-08-07.
 */

(function(){


    angular.module('shortener')
        .controller('MainController',['$log','$scope','$location', 'ShortenerService', MainController]);

    /**
     * Main application controller.
     * @param $log
     * @param $scope
 * @param ShortenerService
     * @constructor
     */
    function MainController($log, $scope, $location, ShortenerService){

        $log.debug('Main Controller Initialized.');

        var self = this;

        self.encodedUrl = null;
        self.data = {
            'url': null
        };

        self.encode = function(){

            $log.debug('Encode the url.');

            if($scope.shortenerForm.$valid){

                $log.debug(" Form validation complete.");

                ShortenerService.encode(self.data)

                .then(function(data){
                        $log.debug("Url shortened to: " + angular.toJson(data));

                        self.encodedUrl = "http://" + $location.host()
                            //+ ":" + $location.port()
                            + "/" + data.url;

                        $log.debug(self.encodedUrl);
                })
                .catch(function(response){
                        $log.debug("Unable to shorten the url.");
                })
            }
        };
    }


}());
