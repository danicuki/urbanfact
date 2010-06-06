class IncreasePhotoUrlFieldSize < ActiveRecord::Migration
	def self.up
		change_table :facts do |t|
			t.change :image_url, :text
		end
	end

	def self.down
		change_table :facts do |t|
			t.change :image_url, :string, :size => 255
		end  
	end
end
