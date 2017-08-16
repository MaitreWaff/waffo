function update_info_section(){
	update_holder = $('#info-update-holder'); // Recupere le div conteneur des Infos.
	most_recent   = update_holder.find("div:last"); // Obtient le dernier div dans le conteneur des infos.

	$.getJSON("/waffo/update-info-after/" + most_recent.attr('id') + "/",
	function(data){
		jQuery.each(data, function(){
			content_to_update = $('div.last-info');
			content_to_update.replaceWith('<div class="panel-body last-info" id="'
			+ this.pk +'"><h1><a target="_blank" href="' + this.fields.link + '">' + this.fields.titre + '</a></h1>'
			+ '<p><a target="_blank" href="' + this.fields.link +'"><img src="/waffo/media/'
			+ this.fields.photo + '" alt="Photo De la Derniere Info" width="225" height="225"></img></a></p><p>'
			+ this.fields.desc + '</p></div>');
		});
	}
	); // Fonction JSON pour emettre la requete et parser la reponse a la requete.
}
function update_astuce_section(){
	update_holder = $('#astuce-update-holder'); // Recupere le div conteneur des Astuces.
	most_recent   = update_holder.find("div:last"); // Obtient le dernier div dans le conteneur des infos.

	$.getJSON("/waffo/update-astuce-after/" + most_recent.attr('id') + "/",
	function(data){
		jQuery.each(data, function(){
			content_to_update = $('div.last-astuce');
			content_to_update.replaceWith('<div class="panel-body last-astuce" id="'
			+ this.pk +'"><h1><a target="_blank" href="' + this.fields.link + '">' + this.fields.titre + '</a></h1>'
			+ '<p><a target="_blank" href="' + this.fields.link +'"><img src="/waffo/media/'
			+ this.fields.photo + '" alt="Photo De la Derniere Astuce" width="225" height="225"></img></a></p><p>'
			+ this.fields.desc + '</p></div>');
		});
	}
	); // Fonction JSON pour emettre la requete et parser la reponse a la requete.
}

function update_articles(){
	update_info_section();
	update_astuce_section();
}



$(document).ready(function(){
//    $(function () {
//      $('[data-toggle="popover"]').popover()
//    })
	setInterval("update_articles()", 3000000); // On rafraichit le contenu toutes les minutes (60.000 millisecondes).
});