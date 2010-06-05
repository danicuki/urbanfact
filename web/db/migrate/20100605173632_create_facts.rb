class CreateFacts < ActiveRecord::Migration
  def self.up
    create_table :facts do |t|
      t.string :description
      t.string :image_url
      t.integer :score
      t.string :hash_tag
			t.integer :lat
			t.integer :lng
			t.date :timestamp 

      t.timestamps
    end
  end

  def self.down
    drop_table :facts
  end
end
