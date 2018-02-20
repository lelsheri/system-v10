frappe.pages['welcome-to-erpnext'].on_page_load = function(wrapper) {
	var parent = $('<div class="welcome-to-erpnext"></div>').appendTo(wrapper);

	parent.html(frappe.render_template("welcome_to_erpnext", {}));

	parent.find(".video-placeholder").on("click", function() {
		window.erpnext_welcome_video_started = true;
		parent.find(".video-placeholder").addClass("hidden");
		parent.find(".embed-responsive").append('<iframe class="embed-responsive-item video-playlist" src="https://www.youtube.com/channel/UCReOlNC-vrX2k5Wut6aF7Dw" allowfullscreen></iframe>')
	});

	// pause video on page change
	$(document).on("page-change", function() {
		if (window.erpnext_welcome_video_started && parent) {
			parent.find(".video-playlist").each(function() {
				this.contentWindow.postMessage('{"event":"command","func":"' + 'pauseVideo' + '","args":""}', '*');
			});
		}
	});
}
