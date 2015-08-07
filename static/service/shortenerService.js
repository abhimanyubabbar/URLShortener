/**
 * Created by babbarshaer on 2015-08-07.
 */

(function(){

    angular.module('shortener')
        .service('ShortenerService', ['$log', ShortenerService]);


    /**
     * Angular Service to interact with the
     * url shortening service.
     *
     * @param $log
     * @constructor
     */
    function ShortenerService($log){


        return {
            encode: encode
        };


        function encode(obj){

            $log.debug("Call to encode the url");

            return $http({
                method:'POST',
                url:'/encode',
                data: obj
            })
                .then(httpSuccess)
                .catch(httpError)
        }


        function httpSuccess(response){

            $log.debug("Http call successful");
            return response.data;
        }

        function httpError(response){

            $log.warn("Http call unsuccessful");
            return $q.reject("Call to service failed with reject error " + response.status);
        }
    }

}());