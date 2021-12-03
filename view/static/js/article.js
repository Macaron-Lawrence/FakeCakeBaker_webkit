

$(document).ready(function () {

    $(".text_main p").each(function(){
        $(this).html($(this).html().replace(/“|”|《|》|（|）/gi, function(matched){
            return mapper[matched];
        }))
    });

}
);

var mapper = {
    "“":"<span>“</span>",
    "”":"<span>”</span>",
    "《":"<span>《</span>",
    "》":"<span>》</span>",
    "（":"<span>（</span>",
    "）":"<span>）</span>"
}
