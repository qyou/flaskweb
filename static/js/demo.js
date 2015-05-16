$("#btn-login").click(function() {
	$("input[name=username]").focus();
});

function isNullOrEmpty(o) {
	return o === undefined || o == null || o.trim() == "";
}

function validate() {
	var name = $("input[name=sign-username]").val();
	var password = $("input[name=sign-password]").val();
	var password_repeat = $("input[name=password-repeat]").val();

	if (isNullOrEmpty(name) || isNullOrEmpty(password) || isNullOrEmpty(password_repeat)) {
		alert("用户名和密码不能为空！");
		return false;
	} else {
		if (password != password_repeat) {
			alert("两次密码不一致，请重新输入");
			$("input[name=password-repeat]").val("");
			return false;
		}
		return true;
	}
}

 $.fn.smartFloat = function() {
        var position = function(element) {
            var top = element.position().top,
            pos = element.css("position");
            $(window).scroll(function() {
                var scrolls = $(this).scrollTop();
                if (scrolls > top) {
                    if (window.XMLHttpRequest) {
                        element.css({
                            position: "fixed",
                            top: 0
                        });
                    } else {
                        element.css({
                            top: scrolls
                        });
                    }
                } else {
                    element.css({
                        position: "absolute",
                        top: top
                    });
                }
            });
        };
        return $(this).each(function() {
            position($(this));
        });
    };
    //绑定,将引号中的内容替换成你想要下拉的模块的ID或者CLASS名字,如"#ABC",".ABC"
    $(".sidebar").smartFloat();