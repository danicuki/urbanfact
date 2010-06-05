# Be sure to restart your server when you modify this file.

# Your secret key for verifying cookie session data integrity.
# If you change this key, all old sessions will become invalid!
# Make sure the secret is at least 30 characters and all random, 
# no regular words or you'll be exposed to dictionary attacks.
ActionController::Base.session = {
  :key         => '_urbanfact_session',
  :secret      => 'fa806d3fd785789aab7f64315c136cea58f0954e89556a7f287a0b58dcb2b320decd301f5be26c0773c7d624df7d2247948370e7404bd9964dc55d3d60c9bd45'
}

# Use the database for sessions instead of the cookie-based default,
# which shouldn't be used to store highly confidential information
# (create the session table with "rake db:sessions:create")
# ActionController::Base.session_store = :active_record_store
