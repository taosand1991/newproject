
$(document).ready(function() {

        $("h3")
            .on('mouseover', function () {
            $(this).css('color', 'red')
        }).on('mouseout', function () {
            $(this).css('color', 'black')
        });
        $(function () {
            $('a').hover(function () {
                $(this).addClass('hovered');
            },function () {
                $(this).removeClass('hovered')
            })
        })


  //
  //  $( "p" )
  // .on( "mouseenter", function() {
  //   $( this ).css({
  //     "background-color": "yellow",
  //     "font-weight": "bolder"
  //   });
  // })
  // .on( "mouseleave", function() {
  //   var styles = {
  //     backgroundColor : "#ddd",
  //     fontWeight: ""
  //   };
  //   $( this ).css( styles );
  // });




});

