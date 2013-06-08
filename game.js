require(['gma/base', 'gma/manager'],

    function(gma) {
        var manager = gma.manager({
            width : 600,
            height : 500
        });
        var myLevel = {
            entities : [
                {top:0, left:0, width:30, height:3},
                {top:0, left:36, width:30, height:3}
            ]
        };
        manager.storeLevels(myLevel);
        manager.init();
    }
);