class DLGrader
  VERBOSE = false

  def initialize(base_dir, code_dir)
    @base_dir, @code_dir = base_dir, code_dir
    @base_dir += "/" if base_dir[-1] != "/"
    @code_dir += "/" if code_dir[-1] != "/"
  end
  
  def grade_all
    Dir.foreach(@base_dir) do |sub_dir_name|
      yield grade sub_dir_name if sub_dir_name != "." and sub_dir_name != ".." and sub_dir_name != ".svn" 
    end
  end
  
  def grade(sub_dir_name)
    number = sub_dir_name[3...sub_dir_name.length].center(10)
    err2null = "2>/dev/null"
    source_path = @base_dir + sub_dir_name + "/lab1"
    bits_c = @code_dir + "/bits.c"
    dlc = @code_dir + "/dlc #{err2null}"
      
    # 1. generate zapped bits.c from source bits.c
    `#{dlc} -z -o #{bits_c} #{source_path}/bits.c`
    return error(number, "compile error") if $? != 0
   
    # 2. make the project
    `cd #{@code_dir} && make #{err2null}`
    return error(number, "compile error") if $? != 0
    
    # 3. stat basic grade of each function
    funs = Hash.new(0.0)
    `#{@code_dir}/btest`.scan(/Test (\w+) score: (\d.\d\d)/) { |match| funs[match[0]] = { basic: Float(match[1]), perf: 0.0 } }
    return error(number, "info missing") if $? != 0
    
    # 4. stat performance grade of each function
    `#{dlc} -e #{bits_c}`.split(/\n/).each do |line|
      fields = line.split(/:/)
      fun = fields[3]
      opers = fields[4]
      funs[fun][:perf] = 2.0 if funs[fun] and funs[fun][:basic] > 0.0 and opers != " Warning"
    end

    # 5. sum up and output
    basic = perf = 0.0
    funs.each do |key, value|
      basic += value[:basic]
      perf += value[:perf]
    end
    total = basic + perf
    VERBOSE ? "number: #{number}, total: #{total} (#{basic} + #{perf})" : "#{number}, #{total}"
  end
  
private
  def error(number, msg)
    VERBOSE ? "number: #{number}, total: 00.0 (#{msg})" : "#{number}, 00.0"
  end
end

DLGrader.new("/home/lewis/ics-se11", "/home/lewis/lab1").grade_all { |res| puts res }
