require 'grit'
include Grit
module MCollective
    module Agent
        class Git<RPC::Agent
            metadata    :name        => "git",
                        :description => "An MCollective client to pull a git repo ", 
                        :author      => "Me",
                        :license     => "MIT/X11",
                        :version     => "0.1",
                        :url         => "http://www.threedrunkensysadsonthe.net",
                        :timeout     => 60

            action "pull" do
		validate :repopath, String
		
		retval = ""

		# setup the git repo
		repo = Repo.new(request[:repopath])
		reply.data = "Updating #{request[:repopath]}"
		repo.pull
		reply.data = "Update completed"
                
            end
        end
    end
end
