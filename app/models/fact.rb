class Fact < ActiveRecord::Base
	has_many :metadatas
	
	def small_description
		return description if description.size <= 20
		"#{description[0..19]}..."
	end
end
