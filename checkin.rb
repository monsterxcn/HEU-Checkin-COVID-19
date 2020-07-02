#!/usr/bin/env ruby
# frozen_string_literal: true

require 'watir'




USERNAME = myid
PASSWORD = mypass

puts '========================='
browser = Watir::Browser.new :chrome, headless: true
browser.goto 'http://ehome.hrbeu.edu.cn/'

def login(browser, username, password)
  browser.text_field(id: 'username').set username
  browser.text_field(id: 'password').set password
  browser.button(name: 'submit').click
end

# First login
login(browser, USERNAME, PASSWORD)
puts 'Login ehome success...'

# Second login
browser.goto 'https://one.wvpn.hrbeu.edu.cn/infoplus/form/JKXXSB/start'
login(browser, USERNAME, PASSWORD)
puts 'Login one success...'

# Wait for loading
browser.wait_until do |b|
  b.div(id: 'div_loader').style.include?('display: none;')
end
puts 'Form loaded...'

# Select the checkbox
cb = browser.checkbox(id: 'V1_CTRL82')
cb.set unless cb.set?
puts 'Checkbox checked...'

# Submit
browser.link(text: '确认填报').click
sleep 5
browser.button(text: '好').click
puts 'Submitted'
sleep 5
browser.button(text: '确定').click

# Check success
browser.refresh
browser.wait_until do |b|
  b.div(id: 'div_loader').style.include?('display: none;')
end
puts browser.div(id: 'title_content').text
if browser.div(id: 'title_content').text.include?('已完成')
  puts 'Checkin Success!'
else
  puts 'Checkin Fail!'
end
puts 'End at ' + Time.now.to_s + '.'
browser.close
puts '========================='