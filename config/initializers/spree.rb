# Configure Spree Preferences
#
# Note: Initializing preferences available within the Admin will overwrite any changes that were made through the user interface when you restart.
#       If you would like users to be able to update a setting with the Admin it should NOT be set here.
#
# In order to initialize a setting do:
# config.setting_name = 'new value'
Spree.config do |config|
  # Example:
  # Uncomment to override the default site name.
  # config.site_name = "Spree Demo Site"
	config.use_s3 = true
	config.s3_bucket = 'globalwoodsource'
	config.s3_access_key = 'tech@globalwoodsource.com'
	config.s3_secret = 'the really good password'
end

Spree.user_class = "Spree::User"

Paperclip.interpolates(:s3_eu_url) do |attachment, style|
	"#{attachment.s3_protocol}://#{Spree::Config[:s3_host_alias]}/#{attachment.globalwoodsource}/#{attachment.path(style).gsub(%r{^/},"")}"
end
