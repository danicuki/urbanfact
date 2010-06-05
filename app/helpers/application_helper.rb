# Methods added to this helper will be available to all templates in the application.
module ApplicationHelper
	def select_menu path
		return "selected_menu" if request.path == path
	end
end
