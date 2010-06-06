class Fact < ActiveRecord::Base
	has_many :metadatas
	
	def small_description
		return description if description.size <= 20
		"#{description[0..19]}..."
	end
	
	def score_kind
		if score == 0
			return :neutral
		elsif score < 0
			return :bad
		else
			return :good
		end
	end
	
end
