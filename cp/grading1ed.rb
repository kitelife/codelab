class DLGrader
  VERBOSE = false

  def initialize(base_dir)
    @base_dir = base_dir
    @base_dir += "/" if base_dir[-1] != "/"
  end
  
  def grade_all
    Dir.foreach(@base_dir) do |sub_dir_name|
      grade sub_dir_name if sub_dir_name != "." and sub_dir_name != ".." and sub_dir_name != ".svn" 
    end
  end
  
  def grade(sub_dir_name)
    number = sub_dir_name[3...sub_dir_name.length].center(10)
    err2null = "2>/dev/null"
    path = @base_dir + sub_dir_name + "/lab1"
    bits_c = path + "/bits.c"
    bits_org_c = path + "/bits.org.c"
    btest = path + "/btest"
    dlc = path + "/dlc #{err2null}"
    make = "make #{err2null}"
    
    # 1. rename bits.c to bits.org.c
    `mv #{bits_c} #{bits_org_c}`
    if $? != 0
      report_error(number, "file error")
      return
    end
      
    # 2. zap bits.org.c to produce bits.c
    `#{dlc} -z -o #{bits_c} #{bits_org_c}`
    if $? != 0
      report_error(number, "compile error")
      `mv #{bits_org_c} #{bits_c}`
      return
    end
    
    # 3. make the project
    `cd #{path} && #{make}`
    if $? != 0
      report_error(number, "compile error")
      `rm #{bits_c}`
      `mv #{bits_org_c} #{bits_c}`
      return
    end
    
    # 4. stat basic grade of each function
    funs = Hash.new(0.0)
    `#{btest}`.scan(/Test (\w+) score: (\d.\d\d)/) do |match|
      funs[match[0]] = { basic: Float(match[1]), perf: 0.0 }
    end
    if $? != 0
      report_error(number, "info missing")
      `rm #{bits_c}`
      `mv #{bits_org_c} #{bits_c}`
      `cd #{path} && make clean`
      return
    end
    
    # 5. stat performance grade of each function
    `#{dlc} -e #{bits_c}`.split(/\n/).each do |line|
      parts = line.split(/:/)
      fun = parts[3]
      opers = parts[4]
      funs[fun][:perf] = 2.0 if funs[fun] and funs[fun][:basic] > 0.0 and opers != " Warning"
    end
    
    # 6. sum up and output
    basic = 0.0
    perf = 0.0
    funs.each do |key, value|
      basic += value[:basic]
      perf += value[:perf]
    end
    total = basic + perf
    if VERBOSE
      puts "number: #{number}, total: #{total} (#{basic} + #{perf})"
    else
      puts "#{number}, #{total}"
    end
    
    `rm #{bits_c}`
    `mv #{bits_org_c} #{bits_c}`
    `cd #{path} && make clean`
  end
  
private
  def report_error(number, error)
    if VERBOSE
      puts "number: #{number}, total: 00.0 (#{error})"
    else
      puts "#{number}, 00.0"
    end
  end
  
end

grader = DLGrader.new("/home/lewis/ics-se11")
grader.grade_all

