class CreateHashtags < ActiveRecord::Migration
  def self.up
    create_table :hashtags do |t|
      t.string :hashtag
      t.string :last_tweet_id

      t.timestamps
    end
  end

  def self.down
    drop_table :hashtags
  end
end
