$(document).on("submit", "form.ajax", function (e) {

    e.preventDefault();
    var $this = $(this);

    document.onkeydown = function (evt) {
        return false;
    };

    var url = $this.attr("action");
    var method = $this.attr("method");
    var isReload = $this.hasClass("reload");
    var isRedirect = $this.hasClass("redirect");
    var noLoader = $this.hasClass("no-loader");
    var noPopup = $this.hasClass("no-popup");
    var isReset = $this.hasClass('reset');

    if (!noLoader) {
        Swal.showLoading();
    }

    jQuery.ajax({
        type: method,
        url: url,
        dataType: "json",
        data: new FormData(this),
        cache: false,
        contentType: false,
        processData: false,
        success: function (data) {
            if (!noLoader) {
                Swal.hideLoading();
            }

            var message = data["message"];
            var status = data["status"];
            var title = data["title"];
            var redirect = data["redirect"];
            var reset = data["reset"];
            var redirect_url = data["redirect_url"];
            var stable = data["stable"];

            if (status == "success") {
                if (title) {
                    title = title;
                } else {
                    title = "Success";
                }

                function doAfter() {
                    if (stable != "true") {
                        
                        if (isRedirect && redirect === "true") {
                            window.location.href = redirect_url;
                        }
                        if (isReload) {
                            window.location.reload();
                        }
                        if (isReset) {
                            $this[0].reset();
                            $this.find('.select2-hidden-accessible').val(null).trigger('change').click();
                        }

                    }
                }

                if (noPopup) {
                    doAfter();
                } else {
                    Swal.fire({
                        icon: status,
                        title: title,
                        html: message,
                    }).then((result) => {
                        console.log(result.isConfirmed,"ygugjgjb");
                        if (result.isConfirmed) {
                            doAfter();
                        }
                    });
                }
                document.onkeydown = function (evt) {
                    return true;
                };
            } else {
                if (title) {
                    title = title;
                } else {
                    title = "An Error Occurred";
                }

                Swal.fire(title, message, "error");

                if (stable != "true") {
                    window.setTimeout(function () {}, 2000);
                }
                document.onkeydown = function (evt) {
                    return true;
                };
            }
        },
        error: function (data) {
            Swal.hideLoading();

            var title = "An error occurred";
            var message = "An error occurred. Please try again later.";
            document.onkeydown = function (evt) {
                return true;
            };
            Swal.fire(title, message, "error");
        },
    });
});

$( document ).ready(function() {
    console.log( "ready!" );
    $( "input.datepicker" ).datepicker({
        dateFormat: "mm/dd/yy"
        ,	duration: "fast"
      });

});

