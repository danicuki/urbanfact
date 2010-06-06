class ChangeFactTimestampToDateTime < ActiveRecord::Migration
  def self.up
	  change_table :facts do |t|
      t.change :timestamp, :datetime
    end
  end

  def self.down
	  change_table :facts do |t|
      t.change :timestamp, :date
    end
  end
end
