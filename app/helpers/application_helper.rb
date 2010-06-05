# Methods added to this helper will be available to all templates in the application.
module ApplicationHelper
	def select_menu path
		return "selected_menu" if path.include? request.path
	end
	
	def order_link text, order
		url = request.url.gsub(/[&]?order=[^&]+/,"")
		join_symbol = (url =~ /\?/) ? "&" : "?"
		"<a href=\"#{url}#{join_symbol}order=#{order}\">#{text}</a>"
	end
	
end
