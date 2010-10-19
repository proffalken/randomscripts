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
		# setup the git repo
		repo = Repo.new(request[:repopath])
		reply.data = "Updating #{request[:repopath]}"
		repo.pull
		reply.data = "Update completed"
                
            end

	    action "merge" do 
		validate :branch1, String
		validate :branch2, String
		validate :repopath, String

		# setup the repo to be merged
		repo  = Repo.new(request[:repopath])
		reply.data = "Merging #{request[:branch1]} into #{request[:branch2]} on repo #{request[:repopath]}"
		repo.merge([branch1,branch2])
	    end
        end
    end
end
